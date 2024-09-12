#include <stdio.h>
#include <dirent.h>
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <time.h>

#include "./scheduler.h"


size_t total_proc = 0;
Process** processes = NULL;
Process* current_proc = NULL;

ProcessChain* current_proc_node = NULL;
ProcessChain** proc_chain = NULL;
ProcessChain* proc_chain_first_node = NULL;

void setup_chain(){
  proc_chain = (ProcessChain**)calloc(total_proc, sizeof(ProcessChain*)); 
  ProcessChain* last = NULL;
  for(size_t i = 0; i < total_proc; i++){
    ProcessChain* chain_node = (ProcessChain*)calloc(1, sizeof(ProcessChain));
    chain_node->proc = processes[i];
    chain_node->next = NULL;

    if(i == 0)
      proc_chain_first_node = chain_node;

    if(last != NULL)
      last->next = chain_node;

    last = chain_node;
    
    if(i == total_proc-1)
      chain_node->next = proc_chain_first_node;
  }
}

size_t total_idle_proc(){
  size_t counter = 0;
  for(size_t i = 0; i < total_proc; i++)
    if(processes[i]->status == IDLE)
      counter++;
  return counter;
}

bool exclude_file(char* filename){
  char* filenames[3] = {".", "..", ".gitkeep"};
  for(size_t i = 0; i < 3; i++)
    if(strcmp(filenames[i], filename) == 0)
      return true;

  return false;
}

void yield(){
  time_t now = time(NULL);
  printf("\n\nCalled yield function!\n\n");
   
  if(current_proc->status == RUNNING){
    current_proc->status = IDLE;
    current_proc->stop_ref++;
  }


  size_t total_idle = total_idle_proc();
  if(total_idle == 0){
    printf("No more processes to be run!\n\n");
    exit(0);
  }

  if(now - current_proc->start >= 1){
    ProcessChain* new_proc_node = current_proc_node->next;
    while(new_proc_node->proc->status != IDLE)
      new_proc_node = new_proc_node->next;

    current_proc_node = new_proc_node;
    current_proc = new_proc_node->proc;

    printf("Changing to process %ld\n\n", current_proc->pos);
    current_proc->status = RUNNING;
    current_proc->start = time(NULL);
    current_proc->func();
  }
}

void proc_func(){
  switch (current_proc->stop_ref) {
    case 0:
      printf("Inside proc func 1\n");
      printf("sleeping for 1s\n");
      sleep(1);
      yield();
    case 1:
      printf("Inside proc func 2\n");
      yield();
    case 2:
      printf("Inside proc func 3\n");
      printf("sleeping for 1s\n");
      sleep(1);
      current_proc->status = FINISHED;
      yield();
    default:
      return;
  }
}


void clear_pointers(){
  for(size_t i = 0; i < total_proc; i++){
    free(processes[i]);
  }
  free(processes);

  size_t i = 0;
  ProcessChain* proc_node_i = proc_chain_first_node;
  while(i < total_proc){
    free(proc_node_i);
    ProcessChain* next = proc_node_i->next;
    proc_node_i = next;
    i++;
  }
  free(proc_chain);
}



void execute(){
  printf("Starting processes!\n\n");
  current_proc_node = proc_chain_first_node;
  current_proc = proc_chain_first_node->proc;
  current_proc->status = RUNNING;
  current_proc->start = time(NULL);
  current_proc->func();
}

int main(){
  DIR* proc_dir = opendir("./proc");
  if(!proc_dir)
    return 1;

  processes = (Process**)calloc(INITIAL_PROCESS_BATCH, sizeof(Process*));
  
  struct dirent *proc_file;
  while((proc_file = readdir(proc_dir)) != NULL){
    char* filename = proc_file->d_name;

    if(exclude_file(filename))
      continue;
    
    Process* proc = (Process*)calloc(1, sizeof(Process));
    proc->filename = filename;
    proc->pos = total_proc;
    proc->func = &proc_func;
    proc->status = IDLE;
    proc->stop_ref = 0;

    if(total_proc >= INITIAL_PROCESS_BATCH){
      processes = (Process**)realloc(processes, sizeof(Process)*(total_proc+1));
    }
    
    processes[total_proc] = proc;
    total_proc++;

    printf("Process %ld: %s\n", total_proc, filename);
  }

  printf("\n\n");
  if(total_proc <= 0)
    return 0;
  
  setup_chain();
  execute();
  clear_pointers();
  return 0;
}
