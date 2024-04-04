import Foundation

func solution(_ park:[String], _ routes:[String]) -> [Int] {
var x: Int!
var y: Int!
var W = park[0].count
var H = park.count

var _park: [[Character]] = Array(park.enumerated()).map { idx, i in
    let p = Array(i)
    if let findedX = Array(i.enumerated()).firstIndex(where: {$0.element == "S"}) {
        x = findedX
        y = idx
    }
    return p
}

routes.forEach {
    let M = $0.split(separator: " ")
    let R = M[0]
    let N = Int(M[1])!
    
    switch R {
    case "E":
        guard x + N < W else { return }
        for i in (x + 1)..<(x + N + 1) {
            if _park[y][i] == "X" {
                return
            }
        }
        _park[y][x] = "O"
        x += N
        _park[y][x] = "S"
        break
    case "N":
        guard y - N >= 0 else { return }
        for i in (y - N)..<y {
            if _park[i][x] == "X" {
                return
            }
        }
        _park[y][x] = "O"
        y -= N
        _park[y][x] = "S"
    case "W":
        guard x - N >= 0 else { return }
        for i in (x - N)..<x {
            if _park[y][i] == "X" {
                return
            }
        }
        _park[y][x] = "O"
        x -= N
        _park[y][x] = "S"
    default: // S
        guard y + N < H else { return }
        for i in (y + 1)..<(y + N + 1) {
            if _park[i][x] == "X" {
                return
            }
        }
        _park[y][x] = "O"
        y += N
        _park[y][x] = "S"
    }
}
    return [y!, x!]
}