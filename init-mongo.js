db.createUser({
    user: "root_raccoon",
    pwd: "k0CJiHbmdTmjYj",
    roles: [{
            role: "root",
            db: "dataRaccoons",

        },
        {
            role: "root",
            db: "admin",

        }
    ]
})

db.createUser({
    user: "root",
    pwd: "root",
    roles: [{
            role: "readWrite",
            db: "dataRaccoons",

        },
        {
            role: "root",
            db: "admin",

        }
    ]
})