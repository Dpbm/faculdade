struct Node{
    value: u32,
    left: Option<Box<Node>>,
    right: Option<Box<Node>>
}

struct Queue<'a>{
    values: Vec<&'a Node>,
}

impl<'a> Queue<'a>{
    fn push(&mut self, element:&'a Node){
        let _ = &self.values.push(element);
    }
    fn pop(&mut self){
        let _ = &self.values.remove(0);
    }
    fn head(&self) -> &'a Node{
        &self.values[0]
    }        
    fn is_empty(&self) -> bool{
        self.values.is_empty()
    }
}

fn append_node(tree:&mut Node, new_node:Node){
    if new_node.value <= tree.value{
        match &mut tree.left{
            Some(subtree) => append_node(subtree, new_node),
            None => tree.left = Some(Box::new(new_node))
        }
    }else{
        match &mut tree.right{
            Some(subtree) => append_node(subtree, new_node),
            None => tree.right = Some(Box::new(new_node))
        }
    }
}

fn create_node(value:u32) -> Node{
    Node{
        value: value,
        left: None,
        right:None
    }
}

fn create_heap(root:&Node) -> Vec<u32>{
    let mut queue = Queue{ values: Vec::new() };
    let mut values = Vec::new();

    queue.push(root);

    loop{
        
        let current_node = queue.head();
        values.push(current_node.value);

        match &current_node.left{
            Some(node) => queue.push(node),
            None => println!("No Left Node")
        }

        match &current_node.right{
            Some(node) => queue.push(node),
            None => println!("No Right Node")
        }

        queue.pop();

        if queue.is_empty(){
            break
        }
    }

    values
}


fn main(){
    let mut root = create_node(10);
    let n1 = create_node(3);
    let n2 = create_node(100);
    let n3 = create_node(12);
    let n4 = create_node(200);
    let n5 = create_node(121);
    let n6 = create_node(6);
    let n7 = create_node(5);

    append_node(&mut root, n1);
    append_node(&mut root, n2);
    append_node(&mut root, n3);
    append_node(&mut root, n4);
    append_node(&mut root, n5);
    append_node(&mut root, n6);
    append_node(&mut root, n7);

    let heap = create_heap(&root);
    println!("{:?}", heap);

    //println!("{}", root.value);
    //println!("{}", root.left.unwrap().value);
    //println!("{}", root.right.unwrap().value);
}
