import Foundation

func solution(_ players:[String], _ callings:[String]) -> [String] {

    var idToString: [Int: String] = [:]
    var stringToIdx: [String: Int] = [:]
    var idxToId: [Int: Int] = [:]

    var id = 0

    players.forEach {
        idToString[id] = $0
        idxToId[id] = id
        stringToIdx[$0] = id
        id += 1
    }

    var arr: [Int] = Array(0..<players.count)

    // idx
    var callArr = callings.map {
        stringToIdx[$0]
    }

    callArr.forEach {
        let currentIdx = stringToIdx[idToString[$0!]!]!
        let frontIdx = stringToIdx[idToString[$0!]!]! - 1
        
    //    print(currentIdx, frontIdx)
        
        // split
        arr.swapAt(currentIdx, frontIdx)
        
    //    print(arr)
        
        // split id
        let tempId = idxToId[currentIdx]!
        idxToId[currentIdx] = idxToId[frontIdx]!
        idxToId[frontIdx] = tempId
        
        let tempStr = stringToIdx[idToString[idxToId[currentIdx]!]!]
        stringToIdx[idToString[idxToId[currentIdx]!]!] = stringToIdx[idToString[idxToId[frontIdx]!]!]!
        stringToIdx[idToString[idxToId[frontIdx]!]!] = tempStr
    }

    //print(arr.map { idToString[$0]! })

    return arr.map { idToString[$0]! }
}