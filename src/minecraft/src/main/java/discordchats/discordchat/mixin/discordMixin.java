package discordchats.discordchat.mixin;

import discordchats.discordchat.Discordchat;
import net.minecraft.client.gui.screen.TitleScreen;
import org.spongepowered.asm.mixin.Mixin;
import org.spongepowered.asm.mixin.injection.At;
import org.spongepowered.asm.mixin.injection.Inject;
import org.spongepowered.asm.mixin.injection.callback.CallbackInfo;
import net.fabricmc.fabric.api.event.lifecycle.v1.ServerTickEvents;

//@Mixin(ServerTickEvents.class)
//public class discordMixin {
//    @Inject(at = @At("HEAD"), method = "ServerTickEvents()V")
//    private void init(CallbackInfo info) {
//        Discordchat.LOGGER.info("This line is printed by an example mod mixin!");
//    }
//}
