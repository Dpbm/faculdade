struct Node{
    value: u32,
    left: Option<Box<Node>>,
    right: Option<Box<Node>>
}

struct Queue{
    elements: Vec<Box<Node>>
}

impl Queue{
    fn insert(&mut self, node:Box<Node>){
        &self.elements.push(node);
    }
    
    fn pop(&mut self){
        &self.elements.pop();
    }
    
    fn len(&mut self) -> usize{
        (&self.elements).len()
    }
}


impl Node{
    fn left_is_none(&self) -> bool{
        match &self.left{
            Some(_) => false,
            None => true
        }
    }
    
    fn right_is_none(&self) -> bool{
        match &self.right{
            Some(_) => false,
            None => true
        }
    }
}

fn create_node(value:u32) -> Node{
    Node{
        value: value,
        left:None,
        right:None,
    }
}

fn append(tree: &mut Node, new_node: Box<Node>){
    if new_node.value < tree.value {
        
        if tree.left_is_none() {
            tree.left = Some(new_node);
        }else{
            match &mut tree.left{
                Some(subtree) => append(subtree, new_node),
                None => println!("FAILED") 
            }
        }
        
    }else{
        if tree.right_is_none() {
            tree.right = Some(new_node);
        }else{
            match &mut tree.right{
                Some(subtree) => append(subtree, new_node),
                None => println!("FAILED") 
            }
        }
    }
}




fn main() {
    let mut root = create_node(10);
    let second_node = Box::new(create_node(3));
    let third_node = Box::new(create_node(14));
    let forth_node = Box::new(create_node(105));
    
    append(&mut root, second_node);
    append(&mut root, third_node);
    append(&mut root, forth_node);
    
    //let right_node = root.right.unwrap();
    //println!("{}", root.clone().value);
    //println!("root left {}",root.clone().left.unwrap().value);
    //println!("root right {}",right_node.right.unwrap().value);
    //println!("child of right node {}",riht_node.value);
    
}