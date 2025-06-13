---------------------------------BOARD---------------------------------------------

Board = { width=0, height=0, characters={} }

function Board:new(width, height) 
    self.height = height
    self.width = width
    self.characters = {}
    return self
end


function Board:addChar(char)
    self.characters[#self.characters + 1] = char
end

---------------------------------CHARACTERS-----------------------------------------

Directions = {
    UP=0,
    DOWN=1,
    LEFT=2,
    RIGHT=3
}

Characters = {
    Tadpole=0,
    Current=1,
    Duplicator=2,
    Fuser=3,
    Splitter=4,
    Lilly=5,
    Deleter=6
}

Character = {char=Characters.Tadpole, dir=Directions.UP, pos={x=0,y=0}}

function Character:new(char, dir, pos)
    self.char = char
    self.dir = dir
    self.pos = pos
    return self  
end

function create_char(char, dir, pos)
    return Character:new{char=char, dir=dir, pos=pos}
end


return {
    Board,
    Characters,
    Directions,
    create_char
}