package com.maculos.minestatus.utils;

import org.bukkit.Bukkit;
import org.bukkit.ChatColor;
import org.bukkit.Server;
import org.bukkit.entity.Player;

public class stop {
    public void stopServer() {
        Server server = Bukkit.getServer();
        Player[] players = server.getOnlinePlayers().toArray(new Player[0]);
        for (Player player : players) {
            player.kickPlayer(ChatColor.GREEN + "Server Restarting");
        }
        server.shutdown();
    }
}