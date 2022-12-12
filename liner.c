#include <stdio.h>
#include <conio.h>

void main()
{
    int a[100], n, i, m, k = 0;
    printf("Enter the element of size:");
    scanf("%d", &n);
    printf("Enter the printing the element of  Array:\n");
    for (i = 0; i < n; i++)
    {
        scanf("%d", &a[i]);
    }
    printf("Enter an element to search :\n");
    scanf("%d", &m);
    for (i = 0; i < n; i++)
    {
        if (a[i] == m)
        {
            printf("Element found index %d", i);
            k = 1;
            break;
        }
    }
    if (k == 0)
    {
        printf("Element not found");
        getch();
    }
}
