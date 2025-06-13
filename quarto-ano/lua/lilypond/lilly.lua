require "constants"

Board = { width=0, height=0, characters={} }

function Board:new(width, height) 
    self.height = height
    self.width = width
    self.characters = {}
    return self
end

function Board:showMatrix()
    -- for i=1,self.height do
    --     local row = ""
    --     for j=1,self.width do
    --         row = row .. tostring(self.matrix[i][j]) .. " "
    --     end
    --     print(row)
    -- end
end

function Board:addChar(char)
    self.characters[#self.characters + 1] = char
end



---------------------------------CHARACTERS---------------------------------------------
Character = { rep=0, moveFunc=nil, pos={ x=0, y=0 }}

function Character:new(o)
    self.rep = o.rep
    self.moveFunc = o.moveFunc
    self.pos = o.pos
    return self
end

function Character:move()
    self.moveFunc(self)
end

-- local c = Character:new{rep=1, moveFunc=test2, pos={x=1,y=1}}
-- c:move()


characters = {
    TadpoleRight=1,
    TadpoleLeft=2,
    TadpoleUp=3,
    TadpoleDown=4,
}

local tadpoleRightMove = function(self)
    self.pos.x = self.pos.x + 1
end

local tadpoleLeftMove = function(self)
    self.pos.x = self.pos.x - 1
end

local tadpoleUpMove = function(self)
    self.pos.y = self.pos.y - 1
end

local tadpoleDownMove = function(self)
    self.pos.y = self.pos.y + 1
end

tadpoleRight = Character:new{rep=characters.TadpoleRight, moveFunc=tadpoleRightMove, pos={x=0,y=0}}
tadpoleLeft = Character:new{rep=characters.TadpoleLeft, moveFunc=tadpoleLeftMove, pos={x=0,y=0}}
tadpoleUp = Character:new{rep=characters.TadpoleUp, moveFunc=tadpoleUpMove, pos={x=0,y=0}}
tadpoleDown = Character:new{rep=characters.TadpoleDown, moveFunc=tadpoleDownMove, pos={x=0,y=0}}

----------------------------------------------------------------------------------------------------------

b = Board:new(MATRIX_WIDTH, MATRIX_HEIGHT)
b.addChar(tadpoleRight)