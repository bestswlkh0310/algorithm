import Foundation

func solution(_ friends:[String], _ gifts:[String]) -> Int {
    
    // MARK: register
    var dic: [String: Int] = [:]
    var id = 0

    for i in friends {
        dic[i] = id
        id += 1
    }

    let length = friends.count
    var graph = Array(repeating: Array(repeating: 0, count: length), count: length)
    var giftScore = Array(repeating: 0, count: length)

    for i in gifts.map({ $0.split(separator: " ") }) {
        
        let sender = String(i[0])
        let receiver = String(i[1])
        let senderIdx = dic[sender]!
        let receiverIdx = dic[receiver]!
        
        // handle graph
        graph[senderIdx][receiverIdx] += 1
        
        // handle gith score
        giftScore[senderIdx] += 1
        giftScore[receiverIdx] -= 1
    }

    for i in graph {
        print(i)
    }

    for i in giftScore {
        print(i)
    }

    var result = Array(repeating: 0, count: length)

    for (senderIdx, sendedList) in graph.enumerated() {
        for (receiverIdx, receiver) in sendedList.enumerated() {
            let sender = graph[receiverIdx][senderIdx]
            if receiver > sender {
                result[senderIdx] += 1
            } else if receiver == sender && receiverIdx < senderIdx {
                if giftScore[receiverIdx] > giftScore[senderIdx] {
                    result[receiverIdx] += 1
                } else if giftScore[receiverIdx] < giftScore[senderIdx] {
                    result[senderIdx] += 1
                }
            }
        }
    }

    return result.max()!

}