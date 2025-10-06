using LinearAlgebra, Random, Colors

function colorwave(n::Int=10; frames=30)
    for t in 1:frames   
        M = [sin(i*j/3 + t/5) for i in 1:n, j in 1:n]
        maxv, minv = maximum(M), minimum(M)
        normed = (M .- minv) ./ (maxv - minv)
        print("\033[H\033[2J")
        for row in normed
            for val in row 
                c = RGB(val, 0.3, 1 - val)
                rgb = (round(Int, c.r*255), round(Int, c.g*255), round(Int, c.b*255))
                print("\033[38;2;$(rgb[1]);$(rgb[2]);$(rgb[3])m██\033[0m")
            end
            println()
        end
        sleep(0.05)
    end
end 

macro timed(ex)
    quote
        local t0 = time()
        local result = $(esc(ex))
        println("time:" , round(time() - t0, digits=4), "s")
        result
    end 
end

@timed colorwave(12, frames=50)