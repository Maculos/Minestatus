package com.maculos.minestatus;

import com.maculos.minestatus.commands.MineStatusCommands;
import com.maculos.minestatus.schedule.Scheduler;
import com.maculos.minestatus.utils.stop;
import org.bukkit.ChatColor;
import org.bukkit.command.CommandExecutor;
import org.bukkit.plugin.java.JavaPlugin;

public class MineStatus extends JavaPlugin {
    @Override
    public void onEnable() {
        MineStatusCommands cmds = new MineStatusCommands();
        getCommand("shutdown").setExecutor(cmds);
        Scheduler sch = new Scheduler();
        sch.stopServer();
        sch.StopServerMessage();
        getServer().getConsoleSender().sendMessage(ChatColor.GREEN + "[MineStatus] Running.");
    }
    @Override
    public void onDisable() {
        getServer().getConsoleSender().sendMessage(ChatColor.RED + "[MineStatus] Stopping.");
    }
}
