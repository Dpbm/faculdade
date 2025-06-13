from typing import List, Tuple
import numpy as np
from time import sleep

"""
      teu   pai  hoje  foi fui
teu   0      0    0     0   0
pai   0      0    0     0   0
hoje  0      0    0     0   0
foi   0      0    0     0   0
fui   0      0    0     0   0
"""

WORDS = ("teu", "pai", "hoje", "foi", "fui")
TOTAL_WORDS = len(WORDS)

def generate_mask(source:int, target:int):
      m = np.zeros(shape=(TOTAL_WORDS, TOTAL_WORDS))
      for i in range(TOTAL_WORDS):
            m[i][source] = 0.01 if i == target else -0.01
      return m

def encode_initial_state(source:int) -> np.matrix:
      return np.matrix([ [1] if (i==source) else [0] for i in range(TOTAL_WORDS) ])

def feedforward(transitions:np.matrix, source:int, target:int) -> bool:
      initial_state = encode_initial_state(source)
      chain_guess = np.dot(transitions,initial_state) 
      max_prob_index = np.argmax(chain_guess)
      is_correct = max_prob_index == target
      
      if(not is_correct):
            transitions += generate_mask(source, target)

      return is_correct

def encode_word(word:str) -> int:
      return WORDS.index(word)

def encode(words:List[str]) -> Tuple[int]:
      return ( encode_word(word) for word in words ) 

def export(transitions:np.matrix):
      print("Exporting weights....")
      np.save("weights.npy", transitions)

def predict(weights:np.matrix, word:str) -> str:
      encoded_word = encode_word(word)
      initial_state = encode_initial_state(encoded_word)
      predicted = np.argmax( np.dot(weights, initial_state) )
      return WORDS[predicted]


if __name__ == "__main__":
      transitions = np.random.uniform(0,1,size=(TOTAL_WORDS, TOTAL_WORDS))

      steps = 100

      data = [("teu", "pai"), ("pai", "foi"), ("hoje", "fui")]

      print("Training....")
      for instance in data:
            source, target = encode(instance)
            for i in range(steps):
                  correct = feedforward(transitions, source, target)
                  if(correct):
                        break
                  sleep(1)
      print("Predict 'Hoje'")
      print("predicted: ", predict(transitions,  "hoje"))
      print("Predict 'fui'")
      print("predicted: ", predict(transitions,  "fui"))
      export(transitions)      

