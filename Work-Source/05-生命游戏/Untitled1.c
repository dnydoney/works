
#include <GL/glut.h>
#include <cmath>
#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

const int WINDOW_WIDTH = 800, WINDOW_HEIGHT = 800;
const int MAP_SCALE = 10;
const int MAP_SIZE = WINDOW_WIDTH / MAP_SCALE;
int MAP[2][MAP_SIZE][MAP_SIZE];

//采用周期边界
int getXY(int x)
{
	return (x + MAP_SIZE) % MAP_SIZE;
}
void Conway()			//Conway's Game of Life
{
	glClear(GL_COLOR_BUFFER_BIT);
	glColor3f(0.0, 0.4, 0.2);
        //产生初始情况
	srand(time(nullptr));
	for (int i = MAP_SIZE / 4; i <= MAP_SIZE * 3 / 4; i++)
		for (int j = MAP_SIZE / 4; j <= MAP_SIZE * 3 / 4; j++)
			MAP[0][i][j] = rand() & 1;

	bool now = 0;
	while (1)
	{
		glClear(GL_COLOR_BUFFER_BIT);
		glPointSize(MAP_SCALE - 1);
		glBegin(GL_POINTS);
		for (int i = 0; i< MAP_SIZE; i++)
			for (int j = 0; j < MAP_SIZE; j++)
				if (MAP[now][i][j]) glVertex2i(i, j);
		glEnd();
		glFlush();

		now = !now;
		for (int i = 0; i<MAP_SIZE; i++)
			for (int j = 0; j <MAP_SIZE; j++)
			{
				int cnt = MAP[!now][getXY(i + 1)][getXY(j)]
						+ MAP[!now][getXY(i)][getXY(j + 1)]
						+ MAP[!now][getXY(i - 1)][getXY(j)]
						+ MAP[!now][getXY(i)][getXY(j - 1)]
						+ MAP[!now][getXY(i + 1)][getXY(j + 1)]
						+ MAP[!now][getXY(i - 1)][getXY(j + 1)]
						+ MAP[!now][getXY(i + 1)][getXY(j - 1)]
						+ MAP[!now][getXY(i - 1)][getXY(j - 1)];
				if (MAP[!now][i][j])
				{
					if (cnt >= 2 && cnt <= 3 )MAP[now][i][j] = 1;
					else MAP[now][i][j] = 0;
				}
				else
				{
					if (cnt == 3)MAP[now][i][j] = 1;
					else MAP[now][i][j] = 0;
				}
			}
		Sleep(10);
	}
	glFlush();
}

int main(int argc, char**argv)
{
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB);
	glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT);
	glutCreateWindow("Conway's Game of Life");
	glClearColor(1.0, 1.0, 1.0, 0.0);
	glMatrixMode(GL_PROJECTION);
	gluOrtho2D(0.0, GLdouble(MAP_SIZE), 0.0, GLdouble(MAP_SIZE));
	glutDisplayFunc(Conway);
	glutMainLoop();
}
