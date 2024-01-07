fun main() {
    val n = readln().toInt()
    var arr: MutableList<Int> = arrayListOf()
    for(i in 0 until n) {
        val inp = readln()
        try {
            if (inp[1] == 'u') {
                arr.add(inp.split(" ")[1].toInt())
            } else if (inp[0] == 't') {
                println(arr[arr.size - 1])
            } else if (inp == "pop") {
                println(arr.removeLast())
            } else if (inp[0] == 'e') {
                if (arr.size == 0) println("1")
                else println("0")
            } else {
                println(arr.size)
            }
        } catch (e: Exception) {
            println("-1")
        }
        //println(arr)
    }
}