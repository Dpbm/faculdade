use std::fs;

fn main(){
    //let DNA="GATGGAACTTGACTACGTAAATT";
    let DNA = fs::read_to_string("input.txt").expect("Failed to read");
    for letter in DNA.chars(){

        match &letter{
            'T' => print!("U"),
            current => print!("{}", current)
        }
    }
}
