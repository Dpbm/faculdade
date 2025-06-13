file = load("PET.txt")

series = flip(file)
size = length(file)
days = 1:size

function buy = should_by(day, series, look_ahead)

    value = series(:,day)
    size = length(series)

    for 

    if day < size
        before = series(:,day+1)
    endif

    # just to limit the test
    buy = false


endfunction


#plot(days, series)
