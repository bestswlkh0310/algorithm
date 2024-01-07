fun main() {
    val k = readln().toInt()
    for (i in 0 until k) {
        val inp = readln().split(" ").map { it.toInt() }
        val h = inp[0]
        val w = inp[1]
        val n = inp[2]

        val y = (n - 1) % h + 1
        val x =  (n - 1) / h + 1
        //if (y == 1 && n > h) { println("%d%02d".format(n % h + 1, n / h)); continue } // <- 수정
        if (h == 1) { println("1%02d".format(n)); continue }
        println("%d%02d".format(y, x))
    }
}

// 1 2 2 => 102
// 10 10 100 => 1010
// 10 10 99 => 910
// 2 1 2 => 201

// 수정
// 3 2 4 => 201

// 위 아래 매치

// 수정
// 5 10 46 => 110
// 3 12 28 => 110