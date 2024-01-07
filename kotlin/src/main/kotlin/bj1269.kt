fun main() {
    var set1 = hashSetOf<Int>()
    var set2 = hashSetOf<Int>()

    val (a, b) = readln().split(" ").map { it.toInt() }
    readln().split(" ").map { set1.add(it.toInt()) }
    readln().split(" ").map { set2.add(it.toInt()) }

    var set3 = set1.union(set2)
    var set4 = set1.intersect(set2)

    println(set3.subtract(set4).size)
}