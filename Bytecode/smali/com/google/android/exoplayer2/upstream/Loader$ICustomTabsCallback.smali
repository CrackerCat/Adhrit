.class public interface abstract Lcom/google/android/exoplayer2/upstream/Loader$ICustomTabsCallback;
.super Ljava/lang/Object;
.source ""


# annotations
.annotation system Ldalvik/annotation/EnclosingClass;
    value = Lcom/google/android/exoplayer2/upstream/Loader;
.end annotation

.annotation system Ldalvik/annotation/InnerClass;
    accessFlags = 0x609
    name = "ICustomTabsCallback"
.end annotation


# virtual methods
.method public abstract ICustomTabsCallback$Stub()V
    .annotation system Ldalvik/annotation/Throws;
        value = {
            Ljava/io/IOException;,
            Ljava/lang/InterruptedException;
        }
    .end annotation
.end method

.method public abstract onTransact()V
.end method
