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