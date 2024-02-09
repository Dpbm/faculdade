       IDENTIFICATION DIVISION.
       PROGRAM-ID. Fibonacci.

       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01 n PIC 9(2).
       01 FirstValue PIC 9(10) VALUE 1.
       01 SecondValue PIC 9(10) VALUE 1.
       01 Result PIC 9(10) VALUE 1.

       PROCEDURE DIVISION.
           ACCEPT n.
           IF n <= 1 THEN
                   DISPLAY "fibonacci: 1"
           ELSE
                   SUBTRACT 1 FROM n
                   PERFORM Fibonacci n TIMES
                   ADD 1 TO n
                   DISPLAY "fibonacci of " n " is " Result
           END-IF.
           STOP RUN.

       Fibonacci.
           COMPUTE Result = FirstValue+SecondValue.
           MOVE SecondValue TO FirstValue.
           MOVE Result TO SecondValue.
