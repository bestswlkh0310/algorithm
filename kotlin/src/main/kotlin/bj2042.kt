fun main() {
    val (n, m, k) = readln().split(" ").map { it.toLong() }

    val arr: MutableList<Long> = ArrayList(n.toInt() + 1)
    for (i in 1 .. n) {
        //arr[i.toInt()] = readln().toLong()
    }
    for (i in 0 until m + k) {
        var sum = 0L
        var (a, b, c) = readln().split(" ").map { it.toLong() }
        if (a == 1L) {
            arr[b.toInt()] = c
        } else {
            //arr[b]~arr[c]까지의 합
            sum(b, c, arr)
            println(sum)
        }
    }
}
fun sum(b: Long, c: Long, arr: MutableList<Long>) {
    var arr: MutableList<Long> = arr.slice(b.toInt()..c.toInt()).toMutableList()
    var size = (c - b) / 2 + 1
    var tmp: MutableList<Long> = ArrayList<Long>((c.toInt() - b.toInt()) / 2 + 1)
    while (tmp.size != 1) {
        for (i in 1 .. size step 2) {
            tmp.add(arr[i.toInt()] + arr[i.toInt() + 1])
        }
        size = tmp.size.toLong()
        arr = tmp
        tmp = ArrayList(size.toInt())
    }
    print(tmp[0])
}