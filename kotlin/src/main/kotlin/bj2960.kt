fun main() {
    val (a, k) = readln().split(" ").map { it.toInt() }
    var arr: MutableList<Int> = arrayListOf()
    var cnt = 0
    var result = 0
    for (i in 2 .. a) arr.add(i)
    loop@
    while (arr.size != 0) {
//        println(arr)
        var removeArr: MutableList<Int> = arrayListOf()
        val first = arr[0]
        for (i in arr) {
            if (i % first == 0) {
                if (k == cnt) break@loop
                removeArr.add(i)
                cnt++
                result = i
//                println("$i $cnt")
            }
        }
        arr = arr.filter { it !in removeArr }.toMutableList()
    }
    println(result)
}