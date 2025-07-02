from controle import RemoteControl


if __name__ == "__main__":
    remote_control = RemoteControl()
    remote_control.tune_channel(5)
    remote_control.next_channel()