#!/bin/bash

#---------------------------------------------------------------------------------Variable
#-----------------------------Color
RED="\033[31m"
GREEN="\033[32m"
YELLOW="\033[33m"
BLUE="\033[34m"
CYAN="\033[36m"
ENDCOLOR="\033[0m"
LINE0="-----"
LINE1="-----------"
LINE2=$LINE1$LINE1
LINE3=$LINE2$LINE2
LINE4=$LINE3$LINE3
header_color=$YELLOW
verbose_color=$BLUE
header_line=$LINE2

#-----------------------------check_jq_yq
check_jq_yq()
{
    # Check jq
    if ! command -v jq >/dev/null 2>&1; then
        echo "jq not found, installing..."
        if [[ "$OSTYPE" == "darwin"* ]]; then
            brew install jq || { echo "Failed to install jq"; return 1; }
        else
            apt update && apt install jq -y || { echo "Failed to install jq"; return 1; }
        fi
    fi
    
    # Check yq
    if ! command -v yq >/dev/null 2>&1; then
        echo "yq not found, installing..."
        if [[ "$OSTYPE" == "darwin"* ]]; then
            brew install yq || { echo "Failed to install yq"; return 1; }
        else
            apt update && snap install yq || { echo "Failed to install yq"; return 1; }
        fi
    fi
    
    return 0
}
check_jq_yq
#-----------------------------Variable
path="$( cd "$(dirname "$0")" ; pwd -P )"
api_sh=$path/api.sh
config_file=$path/config.yaml
#-----------------------------Config
name=$(yq '.general.name' "$config_file" | tr -d '"')

#---------------------------------------------------------------------------------Menu
#--------------------menu_main
menu_main()
{
    clear
    while true; do
        getHeader
        echo -e  ${YELLOW}"1)  ${GREEN}All" ${ENDCOLOR}
        echo -e  ${YELLOW}"2)  ${GREEN}Install" ${ENDCOLOR}
        echo -e  ${YELLOW}"3)  ${GREEN}Service" ${ENDCOLOR}
        echo -e  ${YELLOW}"4)  ${GREEN}Cron"    ${ENDCOLOR}
        echo -e  ${YELLOW}"5)  ${GREEN}Backup"  ${ENDCOLOR}
        echo -e  ${YELLOW}"6)  ${GREEN}Monitor" ${ENDCOLOR}
        echo -e "${YELLOW}${LINE2}${ENDCOLOR}"
        echo -e  ${YELLOW}"q)  ${GREEN}Exit"    ${ENDCOLOR}
        read -p "Enter your choice [1-6]: " choice
        case $choice in
            1)  clear && all;;
            2)  clear && menu_install;;
            3)  clear && menu_service;;
            4)  clear && menu_cron;;
            5)  clear && menu_backup;;
            6)  clear && monitor;;
            q)  clear && exit;;
            *)  exit;;
        esac
        echo -e "\n"
    done
}

#--------------------menu_install : 1
menu_install()
{
    clear
    while true; do
        getHeader
        echo -e  ${YELLOW}${LINE2}Install        ${ENDCOLOR}
        echo -e  ${YELLOW}"1)  ${GREEN}All"      ${ENDCOLOR}
        echo -e  ${YELLOW}"2)  ${GREEN}Update"   ${ENDCOLOR}
        echo -e  ${YELLOW}"3)  ${GREEN}Upgrade"  ${ENDCOLOR}
        echo -e  ${YELLOW}"4)  ${GREEN}Genaral"  ${ENDCOLOR}
        echo -e  ${YELLOW}"5)  ${GREEN}Nginx"    ${ENDCOLOR}
        echo -e  ${YELLOW}"6)  ${GREEN}Iptables" ${ENDCOLOR}
        echo -e  ${YELLOW}"6)  ${GREEN}Postgres" ${ENDCOLOR}
        echo -e  ${YELLOW}${LINE2}               ${ENDCOLOR}
        read -p "Enter your choice [0-7]: " choice
        case $choice in    
            1)  clear && install_all;;
            2)  clear && install_update;;
            3)  clear && install_upgrade;;
            4)  clear && install_general;;
            5)  clear && install_nginx;;
            6)  clear && install_iptables;;
            7)  clear && install_postgres;;
            q)  clear && menu_main;;
            *)  menu_main;;
        esac
        echo -e "\n"
    done
}

#--------------------menu_service : 2
menu_service()
{
    clear
    while true; do
        getHeader
        echo -e  ${YELLOW}${LINE2}Services           ${ENDCOLOR}
        echo -e  ${BLUE}"${LINE1}All"                ${ENDCOLOR}
        echo -e  ${YELLOW}"1)  ${GREEN}Create"       ${ENDCOLOR}
        echo -e  ${YELLOW}"2)  ${GREEN}Status"       ${ENDCOLOR}
        echo -e  ${YELLOW}"3)  ${GREEN}Stop"         ${ENDCOLOR}
        echo -e  ${YELLOW}"4)  ${GREEN}Start"        ${ENDCOLOR}
        echo -e  ${YELLOW}"5)  ${GREEN}Restart"      ${ENDCOLOR}
        echo -e  ${YELLOW}"6)  ${GREEN}Enable"       ${ENDCOLOR}
        echo -e  ${YELLOW}"7)  ${GREEN}Disable"      ${ENDCOLOR}
        echo -e  ${BLUE}"${LINE1}webapi"             ${ENDCOLOR}
        echo -e  ${YELLOW}"8)  ${GREEN}Create"       ${ENDCOLOR}
        echo -e  ${YELLOW}"9)  ${GREEN}Status"       ${ENDCOLOR}
        echo -e  ${YELLOW}"10) ${GREEN}Stop"         ${ENDCOLOR}
        echo -e  ${YELLOW}"11) ${GREEN}Start"        ${ENDCOLOR}
        echo -e  ${YELLOW}"12) ${GREEN}Restart"      ${ENDCOLOR}
        echo -e  ${YELLOW}"13) ${GREEN}Enable"       ${ENDCOLOR}
        echo -e  ${YELLOW}"14) ${GREEN}Disable"      ${ENDCOLOR}
        echo -e  ${YELLOW}"15) ${GREEN}Monitor"      ${ENDCOLOR}
        echo -e  ${BLUE}"${LINE1}Nginx"              ${ENDCOLOR}
        echo -e  ${YELLOW}"16) ${GREEN}Create API"   ${ENDCOLOR}
        echo -e  ${YELLOW}"17) ${GREEN}Create GUI"   ${ENDCOLOR}
        echo -e  ${YELLOW}"18) ${GREEN}Status"       ${ENDCOLOR}
        echo -e  ${YELLOW}"19) ${GREEN}Stop"         ${ENDCOLOR}
        echo -e  ${YELLOW}"20) ${GREEN}Start"        ${ENDCOLOR}
        echo -e  ${YELLOW}"21) ${GREEN}Restart"      ${ENDCOLOR}
        echo -e  ${YELLOW}"22) ${GREEN}Enable"       ${ENDCOLOR}
        echo -e  ${YELLOW}"23) ${GREEN}Disable"      ${ENDCOLOR}
        echo -e  ${YELLOW}"24) ${GREEN}Monitor"      ${ENDCOLOR}
        echo -e  ${BLUE}"${LINE1}Cron min"           ${ENDCOLOR}
        echo -e  ${YELLOW}"25) ${GREEN}Create"       ${ENDCOLOR}
        echo -e  ${YELLOW}"26) ${GREEN}Status"       ${ENDCOLOR}
        echo -e  ${YELLOW}"27) ${GREEN}Stop"         ${ENDCOLOR}
        echo -e  ${YELLOW}"28) ${GREEN}Start"        ${ENDCOLOR}
        echo -e  ${YELLOW}"29) ${GREEN}Restart"      ${ENDCOLOR}
        echo -e  ${YELLOW}"30) ${GREEN}Enable"       ${ENDCOLOR}
        echo -e  ${YELLOW}"31) ${GREEN}Disable"      ${ENDCOLOR}
        echo -e  ${YELLOW}"32) ${GREEN}Monitor"      ${ENDCOLOR}
        echo -e  ${BLUE}"${LINE1}nats-server"        ${ENDCOLOR}
        echo -e  ${YELLOW}"33) ${GREEN}Create"       ${ENDCOLOR}
        echo -e  ${YELLOW}"34) ${GREEN}Status"       ${ENDCOLOR}
        echo -e  ${YELLOW}"35) ${GREEN}Stop"         ${ENDCOLOR}
        echo -e  ${YELLOW}"36) ${GREEN}Start"        ${ENDCOLOR}
        echo -e  ${YELLOW}"37) ${GREEN}Restart"      ${ENDCOLOR}
        echo -e  ${YELLOW}"38) ${GREEN}Enable"       ${ENDCOLOR}
        echo -e  ${YELLOW}"39) ${GREEN}Disable"      ${ENDCOLOR}
        echo -e  ${YELLOW}"40) ${GREEN}Monitor"      ${ENDCOLOR}
        echo -e  ${BLUE}"${LINE1}Other"              ${ENDCOLOR}
        echo -e  ${YELLOW}"41) ${GREEN}SApp ON"      ${ENDCOLOR}
        echo -e  ${YELLOW}"42) ${GREEN}SApp OFF"     ${ENDCOLOR}
        echo -e  ${YELLOW}"43) ${GREEN}Hotspod ON"   ${ENDCOLOR}
        echo -e  ${YELLOW}"44) ${GREEN}Hotspod OFF"  ${ENDCOLOR}
        echo -e  ${YELLOW}"45) ${GREEN}Wifi Connect" ${ENDCOLOR}
        echo -e  ${YELLOW}${LINE2}                   ${ENDCOLOR}
        read -p "Enter your choice [1-45]: " choice
        case $choice in
            #--------------------------All
            1)  clear && service_create_all;;
            2)  clear && service_control_all status;;
            3)  clear && service_control_all stop;;
            4)  clear && service_control_all start;;
            5)  clear && service_control_all restart;;
            6)  clear && service_control_all enable;;
            7)  clear && service_control_all disable;;
            #--------------------------WebApi
            8)  clear && service_create_webapi ;;
            9)  clear && systemctl status $name"_"webapi.service;;
            10) clear && systemctl stop $name"_"webapi.service;;
            11) clear && systemctl start $name"_"webapi.service;;
            12) clear && systemctl restart $name"_"webapi.service;;
            13) clear && systemctl enable $name"_"webapi.service;;
            14) clear && systemctl disable $name"_"webapi.service;;
            15) clear && journalctl -n 100 -u $name"_"webapi.service -f;;
            #--------------------------Nginx
            16) clear && service_create_nginx_create_api;;
            17) clear && service_create_nginx_create_gui;;
            18) clear && systemctl status nginx;;
            19) clear && systemctl stop nginx;;
            20) clear && systemctl start nginx;;
            21) clear && systemctl restart nginx;;
            22) clear && systemctl enable nginx;;
            23) clear && systemctl disable nginx;;
            24) clear && journalctl -n 100 -u nginx -f;;
            #--------------------------Cron
            25) clear && service_cron_min ;;
            26) clear && systemctl status $name"_"service_cron_min.service;;
            27) clear && systemctl stop $name"_"service_cron_min.timer && systemctl stop $name"_"service_cron_min.service;;
            28) clear && systemctl start $name"_"service_cron_min.timer && systemctl start $name"_"service_cron_min.service;;
            29) clear && systemctl restart $name"_"service_cron_min.timer && systemctl restart $name"_"service_cron_min.service;;
            30) clear && systemctl enable $name"_"service_cron_min.service;;
            31) clear && systemctl disable $name"_"service_cron_min.service;;
            32) clear && journalctl -n 100 -u $name"_"service_cron_min.service -f;;
            #--------------------------Nats
            33) clear && service_create_nats_server ;;
            34) clear && systemctl status $name"_"nats_server.service;;
            35) clear && systemctl stop $name"_"nats_server.service;;
            36) clear && systemctl start $name"_"nats_server.service;;
            37) clear && systemctl restart $name"_"nats_server.service;;
            38) clear && systemctl enable $name"_"nats_server.service;;
            39) clear && systemctl disable $name"_"nats_server.service;;
            40) clear && journalctl -n 100 -u $name"_"nats_server.service -f;;
            #--------------------------Other
            41) clear && service_start_app_enable ;;
            42) clear && service_start_app_disable ;;
            43) clear && service_hotspod_enable ;;
            44) clear && service_hotspod_disable ;;
            45) clear && service_wifi_connect ;;
            q)  clear && menu_main;;
            *)  menu_main ;;
        esac
        echo -e "\n"
    done
}

#--------------------menu_cron : 3
menu_cron()
{
    clear
    while true; do
        getHeader
        echo -e  ${YELLOW}${LINE2}Cron        ${ENDCOLOR}
        echo -e  ${YELLOW}"1) ${GREEN}Daily"  ${ENDCOLOR}
        echo -e  ${YELLOW}"2) ${GREEN}Hourly" ${ENDCOLOR}
        echo -e  ${YELLOW}"3) ${GREEN}Minly"  ${ENDCOLOR}
        echo -e  ${YELLOW}"4) ${GREEN}Backup" ${ENDCOLOR}
        echo -e  ${YELLOW}${LINE2}            ${ENDCOLOR}
        read -p "Enter your choice [0-4]: " choice
        case $choice in            
            1) clear && cron_daily ;;
            2) clear && cron_hourly ;;
            3) clear && cron_minly ;;
            4) clear && cron_backup ;;
            q) clear && menu_main ;;
            *) menu_main ;;
        esac
        echo -e "\n"
    done
}

#--------------------menu_backup : 4
menu_backup()
{
    clear
    while true; do
        getHeader
        echo -e  ${YELLOW}${LINE2}Bckup${ENDCOLOR}
        echo -e  ${YELLOW}"1)  ${GREEN}Backup"      ${ENDCOLOR}
        echo -e  ${YELLOW}"2)  ${GREEN}Push github" ${ENDCOLOR}
        echo -e  ${YELLOW}"3)  ${GREEN}Restore"     ${ENDCOLOR}
        echo -e  ${YELLOW}${LINE2}                  ${ENDCOLOR}
        read -p "Enter your choice [1-3]: " choice
        case $choice in
            1) clear && backup_database ;;
            2) clear && github_push ;;
            3) clear && restore_database ;;
            *) menu_main ;;
        esac
        echo -e "\n"
    done
}

#---------------------------------------------------------------------------------api_interface
api_interface()
{
    # Call any function from api.sh with all arguments passed through
    if declare -f "$1" > /dev/null 2>&1; then
        "$@"
    else
        echo "Error: Function '$1' not found"
        exit 1
    fi
}

#---------------------------------------------------------------------------------Actions
source $api_sh
cd $path
if [  "$1" == "" ]; then menu_main; fi
if [  "$1" != "" ]; then api_interface $1 $2 $3 $4 $5; fi