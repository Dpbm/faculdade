require "constants"
require "utils"

local selected_positions = {}
local play = false

function love.load()
    tadpole = love.graphics.newImage("tadpole.png")
    deleter = love.graphics.newImage("deleter.png")

    start = love.graphics.newImage("start.png")
end

function love.update(dt)
    if love.mouse.isDown(PRIMARY_MOUSE_BUTTON) then
        local x, y = love.mouse.getPosition()

        if y <= (TOP_PADDING*CELL_SIDE) then
            return
        end

        local j = math.floor(x/CELL_SIDE)
        local i = math.floor((y/CELL_SIDE)-TOP_PADDING)
       
        selected_positions[getIndex(i,j)] = true
    end
end

function love.draw()
    love.graphics.clear()

    love.graphics.draw(start, 20, 30)

    for i=0,MATRIX_HEIGHT do 
        for j=0,MATRIX_WIDTH do

            local x = j*CELL_SIDE
            local y = (i+TOP_PADDING)*CELL_SIDE
            
            if selected_positions[getIndex(i,j)] then
                love.graphics.draw(deleter, x,y)
            else
                love.graphics.setColor(1,1,1)
                love.graphics.rectangle("line", x, y, CELL_SIDE,CELL_SIDE)
            end
        

        end
    end
end