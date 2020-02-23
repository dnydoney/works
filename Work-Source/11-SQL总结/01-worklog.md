

###  2020年02月04日
-----------------------------------------------------------------

查询SQL Server最近执行过的SQL语句

查询执行的SQL语句
Select TOP 1000 
       ST.text AS '执行的SQL语句',
       QS.execution_count AS '执行次数',
       QS.total_elapsed_time AS '耗时',
       QS.total_logical_reads AS '逻辑读取次数',
       QS.total_logical_writes AS '逻辑写入次数',
       QS.total_physical_reads AS '物理读取次数',       
       QS.creation_time AS '执行时间' ,  
       QS.*
FROM   sys.dm_exec_query_stats QS
       CROSS APPLY 
sys.dm_exec_sql_text(QS.sql_handle) ST
Where  QS.creation_time > dateadd(minute,-1,GETDATE()) --当前时间前一分钟

-- Where QS.creation_time BETWEEN '2015-08-01 00:00:00' AND '2015-09-02 11:00:00' 
ORDER BY QS.total_elapsed_time DESC 




###  2020年02月03日
-----------------------------------------------------------------

https://www.cnblogs.com/aaronguo/p/11174897.html
https://docs.microsoft.com/zh-cn/previous-versions/office/performancepoint-server-2007/bb838723(v=office.12)?redirectedfrom=MSDN

SQL Server 运行状况监控SQL语句

Microsoft SQL Server 2005 提供了一些工具来监控数据库。方法之一是动态管理视图。动态管理视图 (DMV) 和动态管理函数 (DMF) 返回的服务器状态信息可用于监控服务器实例的运行状况、诊断问题和优化性能。

常规服务器动态管理对象包括：

dm_db_*：数据库和数据库对象
dm_exec_*：执行用户代码和关联的连接
dm_os_*：内存、锁定和时间安排
dm_tran_*：事务和隔离
dm_io_*：网络和磁盘的输入/输出
此部分介绍为监控 SQL Server 运行状况而针对这些动态管理视图和函数运行的一些常用查询。

示例查询
您可以运行以下查询来获取所有 DMV 和 DMF 名称：

 
SELECT * FROM sys.system_objects
WHERE name LIKE 'dm_%'
ORDER BY name
 

监控 CPU 瓶颈
CPU 瓶颈通常由以下原因引起：查询计划并非最优、配置不当、设计因素不良或硬件资源不足。下面的常用查询可帮助您确定导致 CPU 瓶颈的原因。

下面的查询使您能够深入了解当前缓存的哪些批处理或过程占用了大部分 CPU 资源。 

SELECT TOP 50 
      SUM(qs.total_worker_time) AS total_cpu_time, 
      SUM(qs.execution_count) AS total_execution_count,
      COUNT(*) AS  number_of_statements, 
      qs.sql_handle 
FROM sys.dm_exec_query_stats AS qs
GROUP BY qs.sql_handle
ORDER BY SUM(qs.total_worker_time) DESC

下面的查询显示缓存计划所占用的 CPU 总使用率（带 SQL 文本）。 

SELECT 
      total_cpu_time, 
      total_execution_count,
      number_of_statements,
      s2.text
      --(SELECT SUBSTRING(s2.text, statement_start_offset / 2, ((CASE WHEN statement_end_offset = -1 THEN (LEN(CONVERT(NVARCHAR(MAX), s2.text)) * 2) ELSE statement_end_offset END) - statement_start_offset) / 2) ) AS query_text
FROM 
      (SELECT TOP 50 
            SUM(qs.total_worker_time) AS total_cpu_time, 
            SUM(qs.execution_count) AS total_execution_count,
            COUNT(*) AS  number_of_statements, 
            qs.sql_handle --,
            --MIN(statement_start_offset) AS statement_start_offset, 
            --MAX(statement_end_offset) AS statement_end_offset
      FROM 
            sys.dm_exec_query_stats AS qs
      GROUP BY qs.sql_handle
      ORDER BY SUM(qs.total_worker_time) DESC) AS stats
      CROSS APPLY sys.dm_exec_sql_text(stats.sql_handle) AS s2
      
      
下面的查询显示 CPU 平均占用率最高的前 50 个 SQL 语句。

SELECT TOP 50
total_worker_time/execution_count AS [Avg CPU Time],
(SELECT SUBSTRING(text,statement_start_offset/2,
(CASE WHEN statement_end_offset = -1 then LEN(CONVERT(nvarchar(max), text)) * 2 ELSE statement_end_offset end -statement_start_offset)/2) 
FROM sys.dm_exec_sql_text(sql_handle)) AS query_text, *
FROM sys.dm_exec_query_stats 
ORDER BY [Avg CPU Time] DESC

下面显示用于找出过多编译/重新编译的 DMV 查询。 

 
select * from sys.dm_exec_query_optimizer_info
where  counter = 'optimizations' or counter = 'elapsed time'
 
 下面的示例查询显示已重新编译的前 25 个存储过程。plan_generation_num 指示该查询已重新编译的次数。

select top 25
      sql_text.text,
      sql_handle,
      plan_generation_num,
      execution_count,
      dbid,
      objectid 
from sys.dm_exec_query_stats a
      cross apply sys.dm_exec_sql_text(sql_handle) as sql_text
where plan_generation_num > 1
order by plan_generation_num desc

效率较低的查询计划可能增大 CPU 占用率。下面的查询显示哪个查询占用了最多的 CPU 累计使用率。

 
 
SELECT 
    highest_cpu_queries.plan_handle, 
    highest_cpu_queries.total_worker_time,
    q.dbid,
    q.objectid,
    q.number,
    q.encrypted,
    q.[text]
from 
    (select top 50 
        qs.plan_handle, 
        qs.total_worker_time
    from 
        sys.dm_exec_query_stats qs
    order by qs.total_worker_time desc) as highest_cpu_queries
    cross apply sys.dm_exec_sql_text(plan_handle) as q
order by highest_cpu_queries.total_worker_time desc
下面的查询显示一些可能占用大量 CPU 使用率的运算符（例如 ‘%Hash Match%’、‘%Sort%’）以找出可疑对象。

 
 
select *
from 
      sys.dm_exec_cached_plans
      cross apply sys.dm_exec_query_plan(plan_handle)
where 
      cast(query_plan as nvarchar(max)) like '%Sort%'
      or cast(query_plan as nvarchar(max)) like '%Hash Match%'
如果已检测到效率低下并导致 CPU 占用率较高的查询计划，请对该查询中涉及的表运行 UPDATE STATISTICS 以查看该问题是否仍然存在。然后，收集相关数据并将此问题报告给 PerformancePoint 规划支持人员。

如果您的系统存在过多的编译和重新编译，可能会导致系统出现与 CPU 相关的性能问题。

您可以运行下面的 DMV 查询来找出过多的编译/重新编译。

 
 
select * from sys.dm_exec_query_optimizer_info
where 
counter = 'optimizations'
or counter = 'elapsed time'
下面的示例查询显示已重新编译的前 25 个存储过程。plan_generation_num 指示该查询已重新编译的次数。

 
 
select top 25
sql_text.text,
sql_handle,
plan_generation_num,
execution_count,
dbid,
objectid 
from sys.dm_exec_query_stats a
cross apply sys.dm_exec_sql_text(sql_handle) as sql_text
where plan_generation_num > 1
order by plan_generation_num desc
如果已检测到过多的编译或重新编译，请尽可能多地收集相关数据并将其报告给规划支持人员

内存瓶颈
开始内存压力检测和调查之前，请确保已启用 SQL Server 中的高级选项。请先对 master 数据库运行以下查询以启用此选项。

 
 
sp_configure 'show advanced options'
go
sp_configure 'show advanced options', 1
go
reconfigure
go
首先运行以下查询以检查内存相关配置选项。

 
 
sp_configure 'awe_enabled'
go
sp_configure 'min server memory'
go
sp_configure 'max server memory'
go
sp_configure 'min memory per query'
go
sp_configure 'query wait'
go
运行下面的 DMV 查询以查看 CPU、计划程序内存和缓冲池信息。

 
 
select 
cpu_count,
hyperthread_ratio,
scheduler_count,
physical_memory_in_bytes / 1024 / 1024 as physical_memory_mb,
virtual_memory_in_bytes / 1024 / 1024 as virtual_memory_mb,
bpool_committed * 8 / 1024 as bpool_committed_mb,
bpool_commit_target * 8 / 1024 as bpool_target_mb,
bpool_visible * 8 / 1024 as bpool_visible_mb
from sys.dm_os_sys_info
I/O 瓶颈
检查闩锁等待统计信息以确定 I/O 瓶颈。运行下面的 DMV 查询以查找 I/O 闩锁等待统计信息。

 
 
select wait_type, waiting_tasks_count, wait_time_ms, signal_wait_time_ms, wait_time_ms / waiting_tasks_count
from sys.dm_os_wait_stats  
where wait_type like 'PAGEIOLATCH%'  and waiting_tasks_count > 0
order by wait_type
如果 waiting_task_counts 和 wait_time_ms 与正常情况相比有显著变化，则可以确定存在 I/O 问题。获取 SQL Server 平稳运行时性能计数器和主要 DMV 查询输出的基线非常重要。

这些 wait_types 可以指示您的 I/O 子系统是否遇到瓶颈。

使用以下 DMV 查询来查找当前挂起的 I/O 请求。请定期执行此查询以检查 I/O 子系统的运行状况，并隔离 I/O 瓶颈中涉及的物理磁盘。

 
 
select 
    database_id, 
    file_id, 
    io_stall,
    io_pending_ms_ticks,
    scheduler_address 
from  sys.dm_io_virtual_file_stats(NULL, NULL)t1,
        sys.dm_io_pending_io_requests as t2
where t1.file_handle = t2.io_handle
在正常情况下，该查询通常不返回任何内容。如果此查询返回一些行，则需要进一步调查。

您还可以执行下面的 DMV 查询以查找 I/O 相关查询。

 
 
select top 5 (total_logical_reads/execution_count) as avg_logical_reads,
                   (total_logical_writes/execution_count) as avg_logical_writes,
           (total_physical_reads/execution_count) as avg_physical_reads,
           Execution_count, statement_start_offset, p.query_plan, q.text
from sys.dm_exec_query_stats
      cross apply sys.dm_exec_query_plan(plan_handle) p
      cross apply sys.dm_exec_sql_text(plan_handle) as q
order by (total_logical_reads + total_logical_writes)/execution_count Desc
下面的 DMV 查询可用于查找哪些批处理/请求生成的 I/O 最多。如下所示的 DMV 查询可用于查找可生成最多 I/O 的前五个请求。调整这些查询将提高系统性能。

 
 
select top 5 
    (total_logical_reads/execution_count) as avg_logical_reads,
    (total_logical_writes/execution_count) as avg_logical_writes,
    (total_physical_reads/execution_count) as avg_phys_reads,
     Execution_count, 
    statement_start_offset as stmt_start_offset, 
    sql_handle, 
    plan_handle
from sys.dm_exec_query_stats  
order by  (total_logical_reads + total_logical_writes) Desc
阻塞
运行下面的查询可确定阻塞的会话。

 
 
select blocking_session_id, wait_duration_ms, session_id from 
sys.dm_os_waiting_tasks
where blocking_session_id is not null
使用此调用可找出 blocking_session_id 所返回的 SQL。例如，如果 blocking_session_id 是 87，则运行此查询可获得相应的 SQL。

 
 
dbcc INPUTBUFFER(87)
下面的查询显示 SQL 等待分析和前 10 个等待的资源。

 
 
select top 10 *
from sys.dm_os_wait_stats
--where wait_type not in ('CLR_SEMAPHORE','LAZYWRITER_SLEEP','RESOURCE_QUEUE','SLEEP_TASK','SLEEP_SYSTEMTASK','WAITFOR')
order by wait_time_ms desc
若要找出哪个 spid 正在阻塞另一个 spid，可在数据库中创建以下存储过程，然后执行该存储过程。此存储过程会报告此阻塞情况。键入 sp_who 可找出 @spid；@spid 是可选参数。

 
 
create proc dbo.sp_block (@spid bigint=NULL)
as
select 
    t1.resource_type,
    'database'=db_name(resource_database_id),
    'blk object' = t1.resource_associated_entity_id,
    t1.request_mode,
    t1.request_session_id,
    t2.blocking_session_id    
from 
    sys.dm_tran_locks as t1, 
    sys.dm_os_waiting_tasks as t2
where 
    t1.lock_owner_address = t2.resource_address and
    t1.request_session_id = isnull(@spid,t1.request_session_id)
以下是使用此存储过程的示例。

 
 
exec sp_block
exec sp_block @spid = 7