1. (Single line comments)

// 10/10/2010 this comment should be deleted
// this comment should not be deleted
int main() {
    std::cout << "Hello World!";
    return 0;
}

2. (Multiline comment)

/* 99/99/9999 this line should be deleted
   this line should be deleted
   this line should also be deleted */

int main() {
    std::cout << "Hello World!";
    return 0;
}

3. (Dates outside of comments)

int main() {
    std::cout << "10/10/1000"; 
    return 0;
}

4. (Dates outside of comments, with a comment starting on the same line)

int main() {
    std::cout << "10/10/1000"; // This is a comment and should not be deleted
    return 0;
}

5. (Wrong comment formats)

// 11/11/1111 this line should be deleted
// 22/2222 this line should not be deleted
// 33/33 this line should not be deleted
// 4444/44/44 this line should not be deleted
// 55/5555/55 this line should not be deleted

int main() {
    std::cout << "Hello World!";
    return 0;
}

6. (Spaced comments)
// 10/10/2010 this comment should be deleted
int main() {
    // this comment should not be deleted
    std::cout << "Hello World!";
    // this comment should 20/20/2020 be deleted
    return 0;
    // th30/30/3000is one should also be deleted
}

7. (Nested comments)
/* this whole line should be deleted /*10/10/1000 including this part
    also this should be deleted too
*/
int main() {
    std::cout << "Hello World!";
    return 0;
}

8. (Dated comment inside nondated comment)

/* this is an ordinary nondated comment and should not be removed
    // 73/82/1964 but what about this line?
*/ 
int main() {
    std::cout << "Hello World!";
    return 0;
}

9. (Right format, wrong symbols)
// 16/10/2024 this is a dated comment and should be removed
// 16/ab/acde however this is not using digits and should not be removed
int main() {
    std::cout << "Hello World!";
    return 0;
}