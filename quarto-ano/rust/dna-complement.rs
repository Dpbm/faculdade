use std::fs;

fn main(){
        //let DNA="AAAACCCGGT";
        let DNA= fs::read_to_string("input2.txt").expect("Failed on reading");
        let mut complete = "".to_owned();
        
        for letter in DNA.chars(){  
            complete.push_str(match &letter{
                'G' => "C",
                'C' => "G",
                'A' => "T",
                'T' => "A",
                _ => ""
            });
        }
        println!("{}", complete.chars().rev().collect::<String>());

}
