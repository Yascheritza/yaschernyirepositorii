#include <stdio.h>
#include<math.h>

void errExit(const char *err) {
    perror(err);
    exit(EXIT_FAILURE);
    }

double f0(double a, double b, double c, double d) {
    return (a*b) - c/d;
    }
double f1(double a) {
    return 3*(pow(a, 3)) - 2*(pow(a, 2)) + log(fabs(a) + 1);
    }
double f2(double a){
    return cos(2*a)*5 - 1;
    }
double f3(double a){
    return pow(M_E, a/2) + 4;
    }
double f4(double a){
    return pow(a, 4) - sqrt(fabs(a));
    }

int main(){
    int start;
    int step;
    int end;
    scanf("%d %d %d", &start, &step, &end);
    start = atof(start);
    step = atof(step);
    end = atof(end);
    output.csv.open() -w -x;
    int dup2(int printf, int STDOUT_FILENO);
    int close(int printf);
    int pfd1[2];
    int pfd2[2];
    int pfd3[2];
    int pfd4[2];
    pipe(pfd1[2]);
    pipe(pfd2[2]);
    pipe(pfd3[2]);
    pipe(pfd4[2]);
    switch (fork()) {
        case 0:
            close(pfd1[0]);
            for (double x = start; x <= end; x+= step) {
                int res = f1(x);
            }
            write(res);
            close(pfd1[1]);
            exit(0);
    switch (fork()) {
        case 0:
            /*2 child here*/
    switch (fork()) {
        case 0:
            /*3 child here*/
    switch (fork()) {
        case 0:
            /*4 child here*/
    close(pfd1[1]);
    close(pfd2[1]);
    close(pfd3[3]);
    close(pfd4[4]);
    if (wait(NULL) == -1) {errExit("wait 1");}
    if (wait(NULL) == -1) {errExit("wait 2");}
    if (wait(NULL) == -1) {errExit("wait 3");}
    if (wait(NULL) == -1) {errExit("wait 4");}
    for (double x = start; x <= end; x += step) {
        double a = read(pfd1[2]);
        double b = read(pfd2[2]);
        double c = read(pfd3[2]);
        double d = read(pfd4[2]);
        double fres = f0(a, b, c, d);
        printf("%d, %d\n", x, fres);
    close(pfd1[0]);
    close(pfd2[0]);
    close(pfd3[0]);
    close(pfd4[0]);
    return 0;
}
