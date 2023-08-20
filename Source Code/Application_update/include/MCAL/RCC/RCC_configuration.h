/*
 * RCC_configuration.h
 *
 *  Created on: Feb 14, 2022
 *      Author: Ashry
 */

#ifndef RCC_CONFIGURATION_H_
#define RCC_CONFIGURATION_H_

/*************************************************************************/
          /*Configurations For Initialization Function */
/*************************************************************************/
/*SELECT SYSTEM CLOCK NEEDED*/
/*options PLL_CLK_SELECT*/
/*        HSE_CLK_SELECT*/
/*        HSI_CLK_SELECT*/
#define CLK_SELECTED		HSI_CLK_SELECT
/*SELECT PLL SOURCE*/
/* options:  HSE_CLK_SELECT*/
/*           HSI_CLK_SELECT*/

#define	PLL_SOURCE_SELECT   HSE_CLK_SELECT

#define HSE_DIVIDED        HSE_DIVIDED_BY_2

/*PLL_MUL_FACTOR OPTIONS*/
/*  PLL_MUL_BY_2
	PLL_MUL_BY_3
	PLL_MUL_BY_4
	PLL_MUL_BY_5
	PLL_MUL_BY_6
	PLL_MUL_BY_7
	PLL_MUL_BY_8
	PLL_MUL_BY_9
	PLL_MUL_BY_10
	PLL_MUL_BY_11
	PLL_MUL_BY_12
	PLL_MUL_BY_13
	PLL_MUL_BY_14
	PLL_MUL_BY_15
	PLL_MUL_BY_16
	PLL_MUL_BY_16
*/


#define PLL_MUL_FACTOR		PLL_MUL_BY_2

/*AHB PRESCALER OPTIONS*/
/*	AHB_PRESCALER_DIVIDED_BY_1
	AHB_PRESCALER_DIVIDED_BY_2
	AHB_PRESCALER_DIVIDED_BY_4
	AHB_PRESCALER_DIVIDED_BY_8
	AHB_PRESCALER_DIVIDED_BY_16
	AHB_PRESCALER_DIVIDED_BY_64
	AHB_PRESCALER_DIVIDED_BY_128
	AHB_PRESCALER_DIVIDED_BY_256
	AHB_PRESCALER_DIVIDED_BY_512
*/
#define AHB_PRESCALER	  AHB_PRESCALER_DIVIDED_BY_1

/*APB1 PRESCALER OPTIONS*/
/* APB1_PRESCALER_DIVIDED_BY_1
   APB1_PRESCALER_DIVIDED_BY_2
   APB1_PRESCALER_DIVIDED_BY_4
   APB1_PRESCALER_DIVIDED_BY_8
   APB1_PRESCALER_DIVIDED_BY_16
*/
#define APB1_PRESCALER	  APB1_PRESCALER_DIVIDED_BY_1

/*APB2 PRESCALER OPTIONS*/
/* APB2_PRESCALER_DIVIDED_BY_1
   APB2_PRESCALER_DIVIDED_BY_2
   APB2_PRESCALER_DIVIDED_BY_4
   APB2_PRESCALER_DIVIDED_BY_8
   APB2_PRESCALER_DIVIDED_BY_16
*/


#define APB2_PRESCALER    APB2_PRESCALER_DIVIDED_BY_1

/*Timeout to Exit Function if clock isnot ready*/

#define CLK_RDY_TIMEOUT  50000






#endif /* RCC_CONFIGURATION_H_ */
