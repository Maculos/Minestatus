package com.maculos.minestatus.commands;

import org.bukkit.command.Command;
import org.bukkit.command.CommandExecutor;
import org.bukkit.command.CommandSender;

import java.util.concurrent.TimeUnit;

public class MineStatusCommands implements CommandExecutor {
    @Override
    public boolean onCommand(CommandSender sender, Command cmd, String label, String[] args) {
        if (cmd.getName().equalsIgnoreCase("shutdown")) {
            int wait = Integer.parseInt(args[0]);
            sender.sendMessage("Shutdown scheduled for " + args[0] + "mins from now.");
        }

        return true;
    }
}
