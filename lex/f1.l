%option noyywrap
%%
stop printf("stop command received!");
start printf("start command received!");
[0-9]+ printf("NUMBER ");
[a-zA-Z][a-zA-Z0-9]* printf("WORD ");
[a-zA-Z0-9\/.-]+ printf("FILENAME ");
\" printf("QUOTE ");
\{ printf("OBRACE ");
\} printf("EBRACE ");
; printf("SEMICOLON ");
\n printf("\n");
[ \t]+ ;
%%
int main(int argc, char* argv[])
{
    yylex();
    return 0;
}
