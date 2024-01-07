fun main() {
    val n = readln().toInt()
    var arr = ArrayDeque<Int>()
    for (i in 1 .. n) {
        arr.add(i)
    }
    while (arr.size != 1 ){
        arr.removeAt(0)
        if (arr.size == 1) break
        arr.add(arr[0])
        arr.removeAt(0)
    }
    println(arr[0])
}