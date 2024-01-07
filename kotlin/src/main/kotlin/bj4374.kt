fun main() {
    try {
        while (true) {
            val n = readln().toInt()
            val arr = arrayListOf<String>().toMutableList()
            val test: MutableList<String> = arrayListOf()
            // p입력
            while (true) {
                val read = readln(); if (read == "EndOfText") break
                val words = read.split(" ").map { word -> word.lowercase().filter { char -> char.code in 97..122 } }.toMutableList()
                words.forEach { arr.add(it) }
                words.forEach { test.add(it) }
            }
            println(test)
            val cntArr: List<String> = arr.distinct()
            val com = arrayListOf<String>()
            cntArr.forEach{c2 ->
                var sum = 0
                arr.forEach { c1 -> if (c1 == c2) sum++ }
                if (sum == n)
                    com.add(c2)
                sum = 0
            }
            if (com.isEmpty()) { println("There is no such word.") }
            else { com.sorted().forEach { println(it) } }
        }
    } catch (_: Exception) {}
}