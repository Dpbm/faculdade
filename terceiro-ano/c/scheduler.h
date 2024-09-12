#ifndef SCHEDULER_H
#define SCHEDULER_H

#define INITIAL_PROCESS_BATCH 4

typedef enum Status{IDLE, RUNNING, FINISHED} Status;

typedef struct Process{
  char *filename;
  size_t pos;
  void (*func)(void);
  time_t start;
  Status status;
  size_t stop_ref;
}Process;

typedef struct ProcessChain{
  Process* proc;
  struct ProcessChain* next;
}ProcessChain;

#endif // ! SCHEDULER_H
