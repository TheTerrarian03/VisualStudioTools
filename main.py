import vcx_utils, file_utils, run_utils, constants

# main function
def main():
    if not run_utils.are_arguments_valid():
        print("\nSorry! Incorrect usage of the tool. Please see the usage below:")
        run_utils.print_usage()
        quit()

    run_args = run_utils.make_run_args()

    print(f"Operation: {run_args.operation_type}")
    print(f"Proj Path: {run_args.project_path}")
    print(f"Args: {run_args.args}   ")

    # at this point are_arguments_valid MUST be true.

    # handle 0 or 1 argument opaerations
    if (run_args.operation_type == "help" or run_args.operation_type == "usage"):
        run_utils.print_usage()
        quit()

    # create and generate project information
    proj_info = run_utils.ProjectInfo()
    proj_info.generate_main_info(run_args.project_path, run_utils.get_project_type_arg(run_args.args))
    proj_info.generate_file_info()

    # print info about the project
    proj_info.display_info()

    # run operation on the project
    if run_args.operation_type == "up":
        # remove unnecessary files if told to
        if "--remove-unnecessary" in run_args.args:
            print("Removing unnecessary files...")
            file_utils.remove_unnecessary_files(proj_info)

        # move the necessary files, creating directories as needed
        file_utils.move_files_to_project_folder(proj_info)
        
        # remove empty folders if told to
        if "--clean-empty" in run_args.args:
            print("Removing empty folders...")
            file_utils.remove_empty_folders(proj_info)

        # create the various files for Visual Studio
        vcx_utils.create_visual_studio_project(proj_info)
    elif run_args.operation_type == "down":
        # Remove all .DS_Store files
        file_utils.remove_DS_Stores(proj_info)
        
        # remove vcx files
        vcx_utils.remove_vcx_files(proj_info)

        # remove vs folders
        vcx_utils.remove_vs_folders(proj_info)

        # move files
        file_utils.move_files_from_project_folder(proj_info)

        # remove empty folders if told to
        if "--clean-empty" in run_args.args:
            print("Removing empty folders...")
            file_utils.remove_empty_folders(proj_info)
    elif run_args.operation_type == "sync":
        print("sync!")
        # do thing
        pass
    elif run_args.operation_type == "ls":
        print("ls!")
        # info already displayed above, do nothing
        pass

    proj_info.display_info()

# run the main function
main()

# def test():
#     for folder_to_remove in constants.VS_UNNECESSARY_FOLDERS:
#         print(folder_to_remove.format(PROJ_NAME="YIPPE"))

# test()