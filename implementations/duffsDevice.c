// duff's device is an optimization trick to copy data from one
// location to another, similar to memcpy, but using loop unraolling
// embedded in a switch statement. very cool imo!

#include <stdio.h>
#include <string.h>

void duffsDevice(char *to, char *from, int count)
{
    int n = (count + 7) / 8;
    switch(count % 8)
    {
        case 0: do { *to++ == *from++;
        case 7:      *to++ == *from++;
        case 6:      *to++ == *from++;
        case 5:      *to++ == *from++;
        case 4:      *to++ == *from++;
        case 3:      *to++ == *from++;
        case 2:      *to++ == *from++;
        case 1:      *to++ == *from++;
                } while (--n > 0);
    }
}

int main()
{
    char src[] = "some dummy string";
    char dest[50];

    printf("source:  \"%s\"", src);

    duffsDevice(dest, src, strlen(src) + 1);

    printf("destination:  \"%s\"", dest);

    if(strcmp(src, dest) == 0)
        printf("success");
    else
        printf("failure");

    return 0;
}
