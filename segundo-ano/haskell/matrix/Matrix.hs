module Matrix ( identity ) where

zeros :: Int -> [Int]
zeros n = take n (repeat 0)

add_one :: Int -> [Int] -> [Int]
add_one i array = (take i array) ++ [1] ++ (take ((length array) - (i+1)) array)

identity :: Int -> [[Int]]
identity n = [add_one i (zeros n) | i <- [0..n-1]]
