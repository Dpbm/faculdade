isOdd :: Int -> Bool
isOdd x = (x `mod` 2) == 1

toString :: Bool -> [Char]
toString x = if x then "True" else "False"

main = do
       input <- getLine
       let x = (read input :: Int)
       print ((toString . isOdd) x)
