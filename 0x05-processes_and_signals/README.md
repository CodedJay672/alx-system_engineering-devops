# Process and Signals
A process can be thought of as an instance of a program in execution. Each time a program is executed, a new instance are created.  
Each process has its own process ID through which it is identified in the system. Each instance has a parent process which also has a parent ID associated with it.  

## The main() Function
C programs always starts with a call to the main() function. The main() function has prototype:  
'int main(int argc, char *argv[]);'  
- the main function has an 'int' return type, which means that, after the function executes, it should return an integer value which is called the status code. This code can be 0 which signifies a successful execution, or any other int value, if the main function's execution failed.  
- The function accepts two arguments:
	- argc: number of command line arguments passed
	- argv: a list of all command line argument. The first argument is the name of the program while other arguments passed consecutively.  
- When a C program is executed by the kernel, an 'exec' function is used to trigger the program.
- Next, a typical startup routing is called just before the main() functionof the program.
- When the program ends execution, a typical end routine is called
- Executable files specify start and end routine addresses as the first routine and the last routine to be called respectively.
- The startup routine takes the command line arguments, environment, etc from the kernel and passes these to the main() function.
- The whole setup is done by the linker in the linking atage of the compilation process.

## Environment List
An env comprises a name=value pairs which represents the shell environment. Similarly, a process also has its environment. There are two ways in which we can access a process environment:  
1. Global variable 'extern char **extern'
2. Passing a third 'char *envp[]' parameter in the main function
**Note**  
- getenv() - gets value of a particular environment variable
- setenv() - sets a new value to an environment variable

## Memory Layout of a Process
Memory layout of a process can be explained in the following manner
- The command line arguments and the environment variables are stored at the top of the process memory layout at the higher addresses
- In the stack, which is the memory area which is used by the process to store local variables of functions and other information that is saved every time a function is called. This information includes the return address from where the function was called, some information on the callers environment like its machines registers etc are stored on a stack. Also, worth mentioning is that anytime a recursive function is called, a new stack frame is generated so that the each set of local variables doesnot interfere with any other set.
- Heap segment is the one which is used for dynamic allocation of memory. This segment is not limited to only one process, instead it is shared among all the processes running on the system. Any process could dynamically allocate memory from this segment. Memory from this segment should be used cautiously and should be deallocated as soon as the process is done using the memory.
- Stack grows downwards while the Heap grows upwards.
- All the global variable which are not initialized in the program are stored in the BSS (Block Started by Symbol) segment. Upon execution, all the unitialized global variables are initialized with the value of zero.
- All initialized global variables are stored in the data segment
- Text segment is the memory location which contains the machine instruction for the CPU. Usually, this segment is shared across different instances of the same program being executed. Since there is no point of changing the CPU instructions so this segment has read-only privileges.
