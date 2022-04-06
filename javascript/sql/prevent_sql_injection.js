const mysql = require('mysql');

const pool = mysql.createPool({
    connectionLimit : 1000, // default = 10
    host: 'localhost',
    user: 'root',
    password: process.env.MYSQL_PW,
    database: 'database_name'
});

function test(req, res) {
    pool.getConnection(function (err, conn) {
        if (err) return console.log(err);

        // use placeholders to prevent the sql injection
        conn.query("SELECT * FROM health_records WHERE dob = ? AND name = ?",[
            req.body.dob,
            req.body.name
        ], (error, results) => {
            if (error) return console.log(error);

            res.send(results);
        })
    });

    // You could also use the named placeholder!
    // <https://coderwall.com/p/196wpg/enable-named-placeholders-in-node-mysql>
}

exports = module.exports = test;