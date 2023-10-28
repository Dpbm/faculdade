import System.IO
import Matrix

main :: IO()
main = do
  let values = identity 10
  putStrLn $ show values

