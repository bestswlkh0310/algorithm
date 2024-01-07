
fun main() {
    var set = hashSetOf<Int>()
    val inp = readln().toInt()
    var first = true

    for (i in 0..<inp) {

        val inp1 = readln().split(" ").map { it.toInt() }

        val n = inp1[0]
        val s = inp1[1]
        val b = inp1[2]

        val tempSet = hashSetOf<Int>()

        val (j1, k1, l1) = n.toString().toList().map { it.toString().toInt() }

        for (j in 1..<10) {
            for (k in 1 ..< 10) {
                for (l in 1 ..< 10) {
                    if (j == k || k == l || j == l) {
                        continue
                    }

                    var strike = 0
                    if (j1 == j || k1 == k || l1 == l) {
                        strike++
                    }

                    var ball = 0
                    if (j != j1 && (j1 == k || j1 == l)) {
                        ball++
                    }
                    if (k != k1 && (k1 == j || k1 == l)) {
                        ball++
                    }
                    if (l != l1 && (l1 == k || l1 == j)) {
                        ball++
                    }

                    if (strike != s || ball != b) {
                        continue
                    }

                    val qq = l + k * 10 + j * 100

                    if (first) {
                        set.add(qq)
                    } else {
                        tempSet.add(qq)
                    }
                }
            }
        }
        if (first) {
            first = false
        } else {
            set = set.intersect(tempSet).toHashSet()
        }
    }
    print(set.size)
}