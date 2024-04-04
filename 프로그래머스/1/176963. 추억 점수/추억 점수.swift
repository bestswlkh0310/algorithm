import Foundation

func solution(_ name:[String], _ yearning:[Int], _ photo:[[String]]) -> [Int] {
    var dict: [String: Int] = [:]
    Array(name.enumerated()).forEach { idx, i in
        dict[i] = yearning[idx]
    }
    return photo.map { people in
        people.map { dict[$0] ?? 0 }.reduce(0, +)
    }
}