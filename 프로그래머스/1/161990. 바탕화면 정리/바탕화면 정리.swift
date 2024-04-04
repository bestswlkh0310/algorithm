import Foundation

func solution(_ wallpaper:[String]) -> [Int] {

    var wallpapers = wallpaper
let graph = wallpapers.map { Array($0) }

let W = graph[0].count
let H = graph.count

var lux = Int.max
var luy = Int.max
var rdx = Int.min
var rdy = Int.min

for y in 0..<H {
    for x in 0..<W {
        if graph[y][x] == "#" {
            lux = min(lux, x)
            luy = min(luy, y)
            rdx = max(rdx, x)
            rdy = max(rdy, y)
        }
    }
}

return [luy, lux, rdy + 1, rdx + 1]
}