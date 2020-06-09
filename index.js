//C: INITAL SET UP
const Discord = require('discord.js');
const bot = new Discord.Client();

//C:DO NOT SHARE THE TOKEN WITH ANYONE 
const token = 'NzE5OTc4MDMxNjk0NzQxNTYy.Xt_Zbg.oxOB9jwyZLrtCxs8Quzuo6acPKY';

//C: CMD SHOWING ITS ONLINE
bot.on('ready', () => {
    Console.log('System is Online!');
})

//C:FEATURES FOR HERE, PLEASE SEPERATE THE CATEGORY:




//C: SYSTEM IS ON
bot.login(token);