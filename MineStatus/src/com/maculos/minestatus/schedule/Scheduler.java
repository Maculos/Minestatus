package com.maculos.minestatus.schedule;

import com.maculos.minestatus.utils.stop;
import org.bukkit.Bukkit;
import org.bukkit.ChatColor;
import org.bukkit.Server;
import org.bukkit.plugin.Plugin;

public class Scheduler {
    static Server server = Bukkit.getServer();
    static Plugin MineStatus = server.getPluginManager().getPlugin("MineStatus");
    int wait = 3000; //pass from command, currently set to 3 mins

    public void stopServer() {
        MineStatus.getServer().getScheduler().scheduleSyncDelayedTask(MineStatus, new Runnable() {
            @Override
            public void run() {
                stop s = new stop();
                s.stopServer();
            }
        }, wait);
    }

    public void StopServerMessage() {
        MineStatus.getServer().getScheduler().scheduleSyncDelayedTask(MineStatus, new Runnable() {
            @Override
            public void run() {
                server.broadcastMessage(ChatColor.DARK_PURPLE + "**Server Restarting in 2min**");
            }
        }, wait - 2400);
    }
}
