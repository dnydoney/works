
###  2019年12月11日
-----------------------------------------------------------------
1.如何使用按键实现长按、短按、多次按下功能


```c
#define KEY_ON          0x01
#define KEY_SET         0x02
#define KEY_UP          0x03
#define KEY_DOW         0x04

#define VALUE_ON        0x05
#define VALUE_SET       0x06
#define VALUE_UP        0x07
#define VALUE_DOW       0x08
#define VALUE_SOUND     0x09
#define KEY_UP_5_TIMES   0x0a

#define  get_key1 		GPIO_ReadInputDataBit(GPIOA,GPIO_Pin_2)
#define  get_key2 		GPIO_ReadInputDataBit(GPIOA,GPIO_Pin_3)
#define  get_key3 		GPIO_ReadInputDataBit(GPIOA,GPIO_Pin_4)
#define  get_key4 		GPIO_ReadInputDataBit(GPIOA,GPIO_Pin_5)

////////////////////////////////////////////////////////////
//按键扫描
//功能说明:获取各个按键的键值
//编程说明:
////////////////////////////////////////////////////////////
void key_scannal(void)			//按键扫描，扫描周期建议2ms
{	static  u16 Key_Read,Key_State,Key_Backup,Key_Long_Delay;//按键去抖时间计时器
	static  u8 click_degree,click_delay;
	static  u16 Key_Delay=50;
	u16 temp_reg1;
	temp_reg1 =0;
	if(!get_key1)	{temp_reg1 =KEY_ON;	}//获取按键值
	if(!get_key2)	{temp_reg1 =KEY_SET;}
	if(!get_key3)	{temp_reg1 =KEY_UP;	}
	if(!get_key4)	{temp_reg1 =KEY_DOW;}
		
 	if(Key_Read !=temp_reg1)	//若按键状态再次改变
	{ 	Key_Read =temp_reg1;	//保存新的按键状态
		Key_Delay =25;			//按键去抖时间初始化,有键值改变从新置初值
	}
	else if(--Key_Delay ==0)	//防抖
	{	
		Key_Delay =100; 			//连调延时50*2ms=100ms
		Key_Touch =Key_Read &(Key_Read ^Key_State);//得出单按键值-次,第二次清掉对应的键值，短按判断看Key_Touch
		Key_State =Key_Read;	//键值保存，长按判断按看Key_State

		if(Key_State ==0)//无按键按下
		{	
			if(++click_delay >=3)	//在有效的时间内连按了几次
			{	
				click_delay =0;
				if(Key_Backup ==KEY_UP)
				{	if(click_degree ==5)	//短按5下
					{	
						Key_Value =KEY_UP_5_TIMES;
					}
				}
				click_degree =0;
				Key_Backup =0;
			}
			Key_Long_Delay =0;		//没有按键值出口
		}
		else
		{	click_delay =0;
			if(++Key_Long_Delay >=30)	Key_Long_Delay =30;
				
			if(Key_Touch ==KEY_ON)		{	;					}
			if(Key_Touch ==KEY_SET)		{Key_Value =VALUE_SET;	}		
			if(Key_State ==KEY_UP)		{Key_Value =VALUE_UP;	}
			if(Key_State ==KEY_DOW)		{Key_Value =VALUE_DOW;	}		
			if(Key_State ==KEY_ON  && Key_Long_Delay ==10)	{Key_Value =VALUE_ON;	}	//长按开关机 200ms*15=3s
			if(Key_State ==KEY_SET && Key_Long_Delay ==10)	{Key_Value =VALUE_SET;	}	//长按设置 10*0.3s=3s
			if(Key_State ==KEY_UP  && Key_Long_Delay ==10)	{Key_Value =VALUE_SOUND;}	//长按加  10*0.3s=3s
			if(Key_State ==KEY_DOW && Key_Long_Delay ==10)	{Key_Value =VALUE_SOUND;}	//长按减  10*0.3s=3s
			if(Key_Touch ==KEY_UP)			//短按5下
			{	
				Key_Backup =KEY_UP;		
				if(click_degree <5)//连击清甲醛
				{
					++click_degree;
				}	
			}


		}
	}
}
////////////////////////////////////////////////////////////
//void KeyProcess(void)
//功能说明:键值处理
////////////////////////////////////////////////////////////
void key_process(void)		//处理周期建议2ms
{
	if(Key_Value ==0)//按键值为0，就不执行下面的程序，减少不必要的判断，提高效率
		return;
	switch(Key_Value)
	{
		case VALUE_ON:
			break;
		case VALUE_SET:
			break;
		case VALUE_UP:
			break;
		case VALUE_DOW:
			break;
		case KEY_UP_5_TIMES:
			break;	
	}
	Key_Value =0;		//清按键值
}
```