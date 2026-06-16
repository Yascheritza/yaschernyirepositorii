#include <stdio.h>
#include <stdlib.h>     // Для atof(), exit()
#include <unistd.h>     // Для fork(), pipe(), dup2(), read(), write(), close()
#include <fcntl.h>      // Для open() и флагов O_WRONLY, O_CREAT, O_TRUNC
#include <sys/wait.h>   // Для wait()
#include <math.h>       // Для математики (pow, log, cos, fabs, exp, sqrt)

void errExit(const char *err) {
    perror(err);
    exit(EXIT_FAILURE);
}

// Функции-варианты
double f0(double a, double b, double c, double d) { return (a * b) - (c / d); }
double f1(double x) { return 3 * pow(x, 3) - 2 * pow(x, 2) + log(fabs(x) + 1); }
double f2(double x) { return cos(2 * x) * 5 - 1; }
// exp(x/2) - это более элегантная замена pow(M_E, x/2) в C
double f3(double x) { return exp(x / 2) + 4; }
double f4(double x) { return pow(x, 4) - sqrt(fabs(x)); }

// argc - количество аргументов, argv - массив строк (аргументов терминала)
int main(int argc, char *argv[]) {
    // 1. ПАРСИНГ АРГУМЕНТОВ
    // Мы берем аргументы прямо из командной строки (argv), а не через scanf.
    // Если передали меньше 4 слов (./exam start step end), ругаемся.
    if (argc != 4) {
        fprintf(stderr, "Usage: %s <start> <end> <step>\n", argv[0]);
        return 1;
    }
    
    // atof переводит текст из консоли ("1.5") в дробное число double
    double start = atof(argv[1]);
    double end   = atof(argv[2]);
    double step  = atof(argv[3]);

    // 2. ПЕРЕНАПРАВЛЕНИЕ ВЫВОДА В ФАЙЛ
    // В C нет метода .open(). Мы используем системный вызов open().
    // Флаги: Писать | Создать если нет | Очистить если есть. 0666 - права доступа.
    int fd = open("output.csv", O_WRONLY | O_CREAT | O_TRUNC, 0666);
    if (fd == -1) errExit("open file");

    // Перепаиваем экран (1) на наш файл (fd)
    if (dup2(fd, STDOUT_FILENO) == -1) errExit("dup2");
    close(fd); // Оригинальный дескриптор файла больше не нужен

    // 3. СОЗДАНИЕ ТРУБ
    // Массив из двух интов: [0] - чтение, [1] - запись
    int pfd1[2], pfd2[2], pfd3[2], pfd4[2];
    if (pipe(pfd1) == -1) errExit("pipe 1");
    if (pipe(pfd2) == -1) errExit("pipe 2");
    if (pipe(pfd3) == -1) errExit("pipe 3");
    if (pipe(pfd4) == -1) errExit("pipe 4");

    // 4. ЗАПУСК ДЕТЕЙ
    // РЕБЕНОК 1
    switch (fork()) {
        case -1: errExit("fork 1");
        case 0:
            close(pfd1[0]); // Закрываем чтение, мы будем только писать
            for (double x = start; x <= end; x += step) {
                double res = f1(x); // Считаем ОДНУ точку
                // Системный вызов write принимает адрес памяти (&res) и количество байт
                write(pfd1[1], &res, sizeof(double)); 
            }
            close(pfd1[1]); // Закрываем кран, сообщая, что данные кончились
            exit(0); // ВАЖНО: Ребенок умирает, чтобы не плодить своих детей!
        default: break; // Родитель идет создавать следующего ребенка
    }

    // РЕБЕНОК 2
    switch (fork()) {
        case -1: errExit("fork 2");
        case 0:
            close(pfd2[0]);
            for (double x = start; x <= end; x += step) {
                double res = f2(x);
                write(pfd2[1], &res, sizeof(double));
            }
            close(pfd2[1]);
            exit(0);
        default: break;
    }

    // РЕБЕНОК 3
    switch (fork()) {
        case -1: errExit("fork 3");
        case 0:
            close(pfd3[0]);
            for (double x = start; x <= end; x += step) {
                double res = f3(x);
                write(pfd3[1], &res, sizeof(double));
            }
            close(pfd3[1]);
            exit(0);
        default: break;
    }

    // РЕБЕНОК 4
    switch (fork()) {
        case -1: errExit("fork 4");
        case 0:
            close(pfd4[0]);
            for (double x = start; x <= end; x += step) {
                double res = f4(x);
                write(pfd4[1], &res, sizeof(double));
            }
            close(pfd4[1]);
            exit(0);
        default: break;
    }

    // 5. РАБОТА РОДИТЕЛЯ
    // Родитель первым делом закрывает все 4 воронки на запись. 
    close(pfd1[1]); close(pfd2[1]); close(pfd3[1]); close(pfd4[1]);

    // Родитель в цикле синхронно читает данные от всех детей
    for (double x = start; x <= end; x += step) {
        double a, b, c, d;
        // Функция read читает СТРОГО размер одного double.
        read(pfd1[0], &a, sizeof(double));
        read(pfd2[0], &b, sizeof(double));
        read(pfd3[0], &c, sizeof(double));
        read(pfd4[0], &d, sizeof(double));

        double fres = f0(a, b, c, d);
        
        // Так как мы сделали dup2 в самом начале, это полетит в output.csv!
        // %f - формат для вывода double.
        printf("%f, %f\n", x, fres); 
    }

    // Родитель дочитал всё, закрываем краны
    close(pfd1[0]); close(pfd2[0]); close(pfd3[0]); close(pfd4[0]);

    // 6. УБОРКА (ЖДЕМ ДЕТЕЙ)
    if (wait(NULL) == -1) errExit("wait 1");
    if (wait(NULL) == -1) errExit("wait 2");
    if (wait(NULL) == -1) errExit("wait 3");
    if (wait(NULL) == -1) errExit("wait 4");

    return 0;
}
