#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

bool is_empty(int a)
{
    if(a==0)
        return true;
    else
        return false;
}

void print_board(int board[3][3])
{
    printf("\n");
    for(int i=0;i<3;i++)
    {
        for(int j=0;j<3;j++)
        {
            printf("%d ", board[i][j]) ;
        }
        printf("\n");
    }
}

void move(int b[3][3],int r,int c,int ch)
{
    int i=0;
    while(i==0)
    {
        if( is_empty(b[r][c]) )
        {
            i=1;
            b[r][c]=ch;
        }
        else
        {
            printf("Place is already occupied. Try again");

        }
    }
}

int check_row(int ch,int board[3][3])
{
    int i,j;
    for(i=0;i<3;i++)
    {
        for(j=0;j<3;j++)
        {
            if(ch!=board[i][j])
            {
                break;
            }
        }
        if(j==3)
        {
            printf("You win");
            return 1;
    }
    else
        return 0;
    }
}

int check_col(int ch,int board[3][3])
{
    int i,j;
    for(i=0;i<3;i++)
    {
        for(j=0;j<3;j++)
        {
            if(ch!=board[j][i])
            {
                break;
            }
        }
        if(j==3)
        {
            printf("You win");
            return 1;
    }
    else
        return 0;
    }
}

int check_diagonal(int ch,int board[3][3])
{
    int i;
    for(i=0;i<3;i++)
    {
        if(board[i][i]!=ch)break;
    }
    for(i=0;i<3;i++)
    {
        if(board[i][2-i]!=ch)break;
    }
    if(i==3)
    {
        printf("You win");
        return 1;
    }
    else
        return 0;
}

int winner(int ch,int board[3][3])
{
    int result=0;
    if( (check_col(ch,board[3][3])==1) || (check_row(ch,board[3][3])==1) || (check_diagonal(ch,board[3][3])==1) )
        result=1;
    return result;
}

int main()
{
    int board[3][3]={0};
    print_board(board);
    int choice;
    printf("Enter your choice 1 or 2 : ");
    scanf("%d",&choice);
    int x=9;
    while(x--)
    {
        printf("Enter the number(for location) as on your numpad : ");
        int i;
        scanf("%d",&i);
        switch(i)
        {
            case 1:
        }
    }
    if(x==0)
    {
        pritnf("\nIt was a tie\nDo you want to play again?(y/n) :");
        char ch;
        scanf("%c",&ch);

    }
    return 0;
}
